%global packname  emme2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Read and Write to an EMME/2 databank

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics 

BuildRequires:    R-devel tex(latex) R-graphics 

%description
This package includes functions to read and write to an EMME/2 databank

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
%doc %{rlibdir}/emme2/html
%doc %{rlibdir}/emme2/DESCRIPTION
%{rlibdir}/emme2/help
%{rlibdir}/emme2/Meta
%{rlibdir}/emme2/NAMESPACE
%{rlibdir}/emme2/INDEX
%{rlibdir}/emme2/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora