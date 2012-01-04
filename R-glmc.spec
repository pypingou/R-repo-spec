%global packname  glmc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Fitting Generalized Linear Models Subject to Constraints

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-emplik 


BuildRequires:    R-devel tex(latex) R-emplik



%description
Fits generalized linear models where the parameters are subject to linear
constraints. The model is specified by giving a symbolic description of
the linear predictor, a description of the error distribution, and a
matrix of constraints on the parameters.

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
%doc %{rlibdir}/glmc/html
%doc %{rlibdir}/glmc/DESCRIPTION
%doc %{rlibdir}/glmc/CITATION
%{rlibdir}/glmc/data
%{rlibdir}/glmc/demo
%{rlibdir}/glmc/Meta
%{rlibdir}/glmc/NAMESPACE
%{rlibdir}/glmc/INDEX
%{rlibdir}/glmc/R
%{rlibdir}/glmc/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora