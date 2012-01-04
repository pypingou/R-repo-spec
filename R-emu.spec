%global packname  emu
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.2.1
Release:          1%{?dist}
Summary:          Interface to the Emu Speech Database System

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-methods R-tcltk R-MASS 

BuildRequires:    R-devel tex(latex) R-stats R-methods R-tcltk R-MASS 

%description
Provides an interface to the Emu speech database system and many special
purpose functions for display and analysis of speech data.

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
%doc %{rlibdir}/emu/DESCRIPTION
%doc %{rlibdir}/emu/html
%{rlibdir}/emu/R
%{rlibdir}/emu/INDEX
%{rlibdir}/emu/NAMESPACE
%{rlibdir}/emu/help
%{rlibdir}/emu/data
%{rlibdir}/emu/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.2.1-1
- initial package for Fedora