%global packname  GrassmannOptim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Grassmann Manifold Optimization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Optimizing a function F(U), where U is a semi-orthogonal matrix and F is
invariant under an orthogonal transformation of U

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
%doc %{rlibdir}/GrassmannOptim/DESCRIPTION
%doc %{rlibdir}/GrassmannOptim/html
%{rlibdir}/GrassmannOptim/R
%{rlibdir}/GrassmannOptim/INDEX
%{rlibdir}/GrassmannOptim/Meta
%{rlibdir}/GrassmannOptim/NAMESPACE
%{rlibdir}/GrassmannOptim/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora