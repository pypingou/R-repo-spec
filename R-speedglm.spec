%global packname  speedglm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Fitting Linear and Generalized Linear Models to large data sets.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Fitting LMs and GLMs to large data sets by updating algorithms.

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
%doc %{rlibdir}/speedglm/html
%doc %{rlibdir}/speedglm/DESCRIPTION
%{rlibdir}/speedglm/NAMESPACE
%{rlibdir}/speedglm/help
%{rlibdir}/speedglm/Meta
%{rlibdir}/speedglm/INDEX
%{rlibdir}/speedglm/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora