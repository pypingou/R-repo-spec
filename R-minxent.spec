%global packname  minxent
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.01
Release:          1%{?dist}
Summary:          Entropy Optimization Distributions

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements entropy optimization distribution under specified
constraints. It also offers an R interface to the MinxEnt and MaxEnt

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
%doc %{rlibdir}/minxent/DESCRIPTION
%doc %{rlibdir}/minxent/html
%{rlibdir}/minxent/help
%{rlibdir}/minxent/Meta
%{rlibdir}/minxent/R
%{rlibdir}/minxent/INDEX
%{rlibdir}/minxent/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.01-1
- initial package for Fedora