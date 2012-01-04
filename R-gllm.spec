%global packname  gllm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.33
Release:          1%{?dist}
Summary:          Generalised log-linear model

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Routines for log-linear models of incomplete contingency tables, including
some latent class models, via EM and Fisher scoring approaches.  Allows

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
%doc %{rlibdir}/gllm/DESCRIPTION
%doc %{rlibdir}/gllm/html
%{rlibdir}/gllm/help
%{rlibdir}/gllm/libs
%{rlibdir}/gllm/Meta
%{rlibdir}/gllm/data
%{rlibdir}/gllm/R
%{rlibdir}/gllm/NAMESPACE
%{rlibdir}/gllm/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.33-1
- initial package for Fedora