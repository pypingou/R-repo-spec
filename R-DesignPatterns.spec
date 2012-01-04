%global packname  DesignPatterns
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Design Patterns in R to build reusable object-oriented software

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Design patterns are building blocks of reusable object-oriented software
projects. This package provides data structures and tools to implement,
study and reuse design patterns, especially the ones introduced in the
book 'Gang of Four'.

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
%doc %{rlibdir}/DesignPatterns/html
%doc %{rlibdir}/DesignPatterns/NEWS
%doc %{rlibdir}/DesignPatterns/DESCRIPTION
%{rlibdir}/DesignPatterns/INDEX
%{rlibdir}/DesignPatterns/Meta
%{rlibdir}/DesignPatterns/NAMESPACE
%{rlibdir}/DesignPatterns/help
%{rlibdir}/DesignPatterns/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora