%global packname  nsRFA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Non-supervised Regional Frequency Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-graphics 

%description
A collection of statistical tools for objective (non-supervised)
applications of the Regional Frequency Analysis methods in hydrology.  The
package refers to the index-value method and, more precisely, helps the
hydrologist to: (1) regionalize the index-value; (2) form homogeneous
regions with similar growth curves; (3) fit distribution functions to the
empirical regional growth curves.

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
%doc %{rlibdir}/nsRFA/html
%doc %{rlibdir}/nsRFA/DESCRIPTION
%doc %{rlibdir}/nsRFA/doc
%{rlibdir}/nsRFA/data
%{rlibdir}/nsRFA/NAMESPACE
%{rlibdir}/nsRFA/help
%{rlibdir}/nsRFA/Meta
%{rlibdir}/nsRFA/demo
%{rlibdir}/nsRFA/R
%{rlibdir}/nsRFA/libs
%{rlibdir}/nsRFA/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.2-1
- initial package for Fedora