%global packname  Rcgmin
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.2.101
Release:          1%{?dist}
Summary:          Conjugate gradient minimization of nonlinear functions with box constraints

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011-2.101.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-numDeriv 

BuildRequires:    R-devel tex(latex) R-numDeriv 

%description
Conjugate gradient minimization of nonlinear functions with box
constraints incorporating Dai/Yuan update

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
%doc %{rlibdir}/Rcgmin/html
%doc %{rlibdir}/Rcgmin/DESCRIPTION
%{rlibdir}/Rcgmin/R
%{rlibdir}/Rcgmin/Meta
%{rlibdir}/Rcgmin/NAMESPACE
%{rlibdir}/Rcgmin/demo
%{rlibdir}/Rcgmin/help
%{rlibdir}/Rcgmin/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.2.101-1
- initial package for Fedora