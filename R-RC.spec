%global packname  RC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2.13
Release:          1%{?dist}
Summary:          Reproducible Computing

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-igraph R-bitops 

BuildRequires:    R-devel tex(latex) R-igraph R-bitops 

%description
The RC package allows the user to create and use reproducible computations
for the purpose of research and education. The meta data about the
computations are stored in a remote repository which is hosted at

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
%doc %{rlibdir}/RC/DESCRIPTION
%doc %{rlibdir}/RC/html
%{rlibdir}/RC/NAMESPACE
%{rlibdir}/RC/help
%{rlibdir}/RC/INDEX
%{rlibdir}/RC/R
%{rlibdir}/RC/Meta
%{rlibdir}/RC/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2.13-1
- initial package for Fedora