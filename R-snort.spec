%global packname  snort
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Social Network-Analysis On Relational Tables

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-network R-sna 

BuildRequires:    R-devel tex(latex) R-network R-sna 

%description
The package creates a triple store in the popular Pajek format.  It also
supports a 3-Dimensional interactive VRML visualisation for network

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
%doc %{rlibdir}/snort/DESCRIPTION
%doc %{rlibdir}/snort/html
%{rlibdir}/snort/help
%{rlibdir}/snort/extdata
%{rlibdir}/snort/Meta
%{rlibdir}/snort/INDEX
%{rlibdir}/snort/LICENSE
%{rlibdir}/snort/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora