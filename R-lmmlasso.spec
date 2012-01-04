%global packname  lmmlasso
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Linear mixed-effects models with Lasso

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-emulator R-miscTools R-penalized 

BuildRequires:    R-devel tex(latex) R-methods R-emulator R-miscTools R-penalized 

%description
This package fits (gaussian) linear mixed-effects models for
high-dimensional data (n<<p) using a Lasso-type approach for the
fixed-effects parameter.

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
%doc %{rlibdir}/lmmlasso/html
%doc %{rlibdir}/lmmlasso/DESCRIPTION
%{rlibdir}/lmmlasso/NAMESPACE
%{rlibdir}/lmmlasso/Meta
%{rlibdir}/lmmlasso/R
%{rlibdir}/lmmlasso/INDEX
%{rlibdir}/lmmlasso/data
%{rlibdir}/lmmlasso/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora