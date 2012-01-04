%global packname  YourCast
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.11
Release:          1%{?dist}
Summary:          YourCast

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-foreign R-lattice 

BuildRequires:    R-devel tex(latex) R-foreign R-lattice 

%description
YourCast makes time series cross-sectional forecasts with multiple
cross-sections based on your assumptions. It allows a variety of smoothing
assumptions based on similarities among the levels, trends, or
interactions in the expected value of the dependent variable rather than
the coefficients.  YourCast implements ideas in the book Federico Girosi
and Gary King. DEMOGRAPHIC FORECASTING. Princeton University Press, 2008;
see http://gking.harvard.edu/files/smooth/

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/YourCast/doc
%doc %{rlibdir}/YourCast/DESCRIPTION
%doc %{rlibdir}/YourCast/html
%{rlibdir}/YourCast/NAMESPACE
%{rlibdir}/YourCast/LICENSE
%{rlibdir}/YourCast/Meta
%{rlibdir}/YourCast/data
%{rlibdir}/YourCast/INDEX
%{rlibdir}/YourCast/R
%{rlibdir}/YourCast/help
%{rlibdir}/YourCast/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.11-1
- initial package for Fedora