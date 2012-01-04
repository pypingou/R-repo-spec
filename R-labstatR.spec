%global packname  labstatR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Libreria del Laboratorio di Statistica con R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Insieme di funzioni di supporto al volume "Laboratorio di Statistica con
R", Iacus-Masarotto, MacGraw-Hill Italia, 2006. This package contains sets
of functions defined in "Laboratorio di Statistica con R",
Iacus-Masarotto, MacGraw-Hill Italia, 2006. Function names and docs are in
italian as well.

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
%doc %{rlibdir}/labstatR/html
%doc %{rlibdir}/labstatR/DESCRIPTION
%{rlibdir}/labstatR/R
%{rlibdir}/labstatR/INDEX
%{rlibdir}/labstatR/NAMESPACE
%{rlibdir}/labstatR/help
%{rlibdir}/labstatR/scripts
%{rlibdir}/labstatR/Meta
%{rlibdir}/labstatR/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora