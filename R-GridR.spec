%global packname  GridR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Executes functions on remote hosts, clusters or grids.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-codetools 

BuildRequires:    R-devel tex(latex) R-codetools 

%description
GridR is an R-Package that can be used to submit R functions for execution
on remote computers, clusters or grids. In addition, users are provided
with an interface to share variables and functions with other users.

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
%doc %{rlibdir}/GridR/html
%doc %{rlibdir}/GridR/DESCRIPTION
%{rlibdir}/GridR/R
%{rlibdir}/GridR/INDEX
%{rlibdir}/GridR/help
%{rlibdir}/GridR/Meta
%{rlibdir}/GridR/NAMESPACE
%{rlibdir}/GridR/GridR

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora