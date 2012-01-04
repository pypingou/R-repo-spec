%global packname  MLDS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Maximum Likelihood Difference Scaling

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-utils R-base 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-utils R-base 

%description
Difference scaling is a method for scaling perceived supra-threshold
differences.  The package contains functions that allow the user to design
and run a difference scaling experiment, to fit the resulting data by
maximum likelihood and test the internal validity of the estimated scale.

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
%doc %{rlibdir}/MLDS/CITATION
%doc %{rlibdir}/MLDS/doc
%doc %{rlibdir}/MLDS/NEWS
%doc %{rlibdir}/MLDS/DESCRIPTION
%doc %{rlibdir}/MLDS/html
%{rlibdir}/MLDS/Meta
%{rlibdir}/MLDS/NAMESPACE
%{rlibdir}/MLDS/R
%{rlibdir}/MLDS/help
%{rlibdir}/MLDS/INDEX
%{rlibdir}/MLDS/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.3-1
- initial package for Fedora