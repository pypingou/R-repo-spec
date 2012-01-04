%global packname  Rfit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.14
Release:          1%{?dist}
Summary:          Rank Estimation for Linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-quantreg 


BuildRequires:    R-devel tex(latex) R-methods R-quantreg



%description
R estimation and inference for linear models.  Estimation is for general
scores and a library of commonly used score functions is included.

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
%doc %{rlibdir}/Rfit/html
%doc %{rlibdir}/Rfit/DESCRIPTION
%{rlibdir}/Rfit/data
%{rlibdir}/Rfit/Meta
%{rlibdir}/Rfit/R
%{rlibdir}/Rfit/help
%{rlibdir}/Rfit/INDEX
%{rlibdir}/Rfit/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.14-1
- initial package for Fedora