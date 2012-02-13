%global packname  LaplacesDemon
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          12.01.02
Release:          1%{dist}
Summary:          Software for Bayesian Inference

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Laplace's Demon is software for Bayesian inference.

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
%doc %{rlibdir}/LaplacesDemon/html
%doc %{rlibdir}/LaplacesDemon/CITATION
%doc %{rlibdir}/LaplacesDemon/DESCRIPTION
%doc %{rlibdir}/LaplacesDemon/doc
%{rlibdir}/LaplacesDemon/NAMESPACE
%{rlibdir}/LaplacesDemon/INDEX
%{rlibdir}/LaplacesDemon/R
%{rlibdir}/LaplacesDemon/Meta
%{rlibdir}/LaplacesDemon/data
%{rlibdir}/LaplacesDemon/help

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 12.01.02-1
- Update to version 12.01.02

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 11.11.03-1
- initial package for Fedora