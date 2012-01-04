%global packname  mixdist
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          Finite Mixture Distribution Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions for fitting finite mixture distribution
models to grouped data and conditional data by the method of maximum
likelihood using a combination of a Newton-type algorithm and the EM

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
%doc %{rlibdir}/mixdist/html
%doc %{rlibdir}/mixdist/DESCRIPTION
%{rlibdir}/mixdist/help
%{rlibdir}/mixdist/INDEX
%{rlibdir}/mixdist/Meta
%{rlibdir}/mixdist/R
%{rlibdir}/mixdist/data
%{rlibdir}/mixdist/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.4-1
- initial package for Fedora