%global packname  dglm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Double generalized linear models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-statmod 

BuildRequires:    R-devel tex(latex) R-statmod 

%description
Fitting double  generalized linear models

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
%doc %{rlibdir}/dglm/html
%doc %{rlibdir}/dglm/DESCRIPTION
%{rlibdir}/dglm/R
%{rlibdir}/dglm/help
%{rlibdir}/dglm/INDEX
%{rlibdir}/dglm/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.1-1
- initial package for Fedora