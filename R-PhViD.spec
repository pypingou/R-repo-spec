%global packname  PhViD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          PhViD: a R package for PharmacoVigilance signal Detection.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-LBE R-MCMCpack R-tcltk 

BuildRequires:    R-devel tex(latex) R-LBE R-MCMCpack R-tcltk 

%description
PhViD contains several pharmacovigilance signal detection methods extended
to the multiple comparison setting. These functions can be used as
standard R functions or through an user friendly interface (PhViD.gui())

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
%doc %{rlibdir}/PhViD/html
%doc %{rlibdir}/PhViD/CITATION
%doc %{rlibdir}/PhViD/DESCRIPTION
%{rlibdir}/PhViD/R
%{rlibdir}/PhViD/Meta
%{rlibdir}/PhViD/help
%{rlibdir}/PhViD/data
%{rlibdir}/PhViD/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora