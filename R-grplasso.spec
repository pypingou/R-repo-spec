%global packname  grplasso
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Fitting user specified models with Group Lasso penalty

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Fits user specified (GLM-) models with Group Lasso penalty

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
%doc %{rlibdir}/grplasso/html
%doc %{rlibdir}/grplasso/DESCRIPTION
%{rlibdir}/grplasso/R
%{rlibdir}/grplasso/data
%{rlibdir}/grplasso/Meta
%{rlibdir}/grplasso/help
%{rlibdir}/grplasso/INDEX
%{rlibdir}/grplasso/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.2-1
- initial package for Fedora