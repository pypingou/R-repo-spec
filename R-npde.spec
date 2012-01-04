%global packname  npde
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Normalised prediction distribution errors for nonlinear mixed-effect models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Routines to compute normalised prediction distribution errors, a metric
designed to evaluate non-linear mixed effect models such as those used in
pharmacokinetics and pharmacodynamics

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
%doc %{rlibdir}/npde/DESCRIPTION
%doc %{rlibdir}/npde/html
%doc %{rlibdir}/npde/doc
%doc %{rlibdir}/npde/citation
%{rlibdir}/npde/Meta
%{rlibdir}/npde/NAMESPACE
%{rlibdir}/npde/R
%{rlibdir}/npde/data
%{rlibdir}/npde/help
%{rlibdir}/npde/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora