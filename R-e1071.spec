%global packname  e1071
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Misc Functions of the Department of Statistics (e1071), TU Wien

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-class 

BuildRequires:    R-devel tex(latex) R-class 

%description
Functions for latent class analysis, short time Fourier transform, fuzzy
clustering, support vector machines, shortest path computation, bagged
clustering, naive Bayes classifier, ...

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
%doc %{rlibdir}/e1071/html
%doc %{rlibdir}/e1071/DESCRIPTION
%doc %{rlibdir}/e1071/doc
%{rlibdir}/e1071/NAMESPACE
%{rlibdir}/e1071/NEWS.Rd
%{rlibdir}/e1071/Meta
%{rlibdir}/e1071/R
%{rlibdir}/e1071/help
RPM build errors:
%{rlibdir}/e1071/libs
%{rlibdir}/e1071/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora