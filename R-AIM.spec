%global packname  AIM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          AIM: adaptive index model

Group:            Applications/Engineering 
License:          LGPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
R functions for adaptively constructing index models for continuous,
binary and survival outcomes. Implementation requires loading R-pacakge

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
%doc %{rlibdir}/AIM/DESCRIPTION
%doc %{rlibdir}/AIM/html
%{rlibdir}/AIM/R
%{rlibdir}/AIM/NAMESPACE
%{rlibdir}/AIM/help
%{rlibdir}/AIM/INDEX
%{rlibdir}/AIM/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora