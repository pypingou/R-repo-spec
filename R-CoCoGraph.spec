%global packname  CoCoGraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7.6
Release:          1%{?dist}
Summary:          Interactive and dynamic graphs for the CoCo objects

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-dynamicGraph R-MASS R-methods R-CoCo 

BuildRequires:    R-devel tex(latex) R-dynamicGraph R-MASS R-methods R-CoCo 

%description
Interface between dynamicGraph and CoCo (objects)

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
%doc %{rlibdir}/CoCoGraph/DESCRIPTION
%doc %{rlibdir}/CoCoGraph/html
%{rlibdir}/CoCoGraph/Meta
%{rlibdir}/CoCoGraph/help
%{rlibdir}/CoCoGraph/LICENSE
%{rlibdir}/CoCoGraph/R
%{rlibdir}/CoCoGraph/INDEX
%{rlibdir}/CoCoGraph/demo
%{rlibdir}/CoCoGraph/NAMESPACE

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7.6-1
- initial package for Fedora