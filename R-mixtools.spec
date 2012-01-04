%global packname  mixtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Tools for analyzing finite mixture models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-MASS 

BuildRequires:    R-devel tex(latex) R-boot R-MASS 

%description
A collection of R functions for analyzing finite mixture models.  This
package is based upon work supported by the National Science Foundation
under Grant No. SES-0518772.

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
%doc %{rlibdir}/mixtools/doc
%doc %{rlibdir}/mixtools/DESCRIPTION
%doc %{rlibdir}/mixtools/CITATION
%doc %{rlibdir}/mixtools/html
%{rlibdir}/mixtools/INDEX
%{rlibdir}/mixtools/Meta
%{rlibdir}/mixtools/data
%{rlibdir}/mixtools/help
%{rlibdir}/mixtools/R
RPM build errors:
%{rlibdir}/mixtools/libs
%{rlibdir}/mixtools/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.4-1
- initial package for Fedora