%global packname  COZIGAM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Constrained and Unconstrained Zero-Inflated Generalized Additive Models with Model Selection Criterion

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mgcv 

BuildRequires:    R-devel tex(latex) R-mgcv 

%description
Constrained and Unconstrained Zero-Inflated Generalized Additive Models
(ZIGAM) fitting with associated model plotting, prediction and selection.

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
%doc %{rlibdir}/COZIGAM/DESCRIPTION
%doc %{rlibdir}/COZIGAM/CITATION
%doc %{rlibdir}/COZIGAM/html
%{rlibdir}/COZIGAM/R
%{rlibdir}/COZIGAM/help
%{rlibdir}/COZIGAM/INDEX
%{rlibdir}/COZIGAM/data
%{rlibdir}/COZIGAM/NAMESPACE
%{rlibdir}/COZIGAM/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.3-1
- initial package for Fedora