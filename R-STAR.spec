%global packname  STAR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Spike Train Analysis with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-mgcv R-R2HTML R-gss R-codetools 


BuildRequires:    R-devel tex(latex) R-survival R-mgcv R-R2HTML R-gss R-codetools



%description
Functions to analyze neuronal spike trains from a single neuron or from
several neurons recorded simultaneously.

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
%doc %{rlibdir}/STAR/html
%doc %{rlibdir}/STAR/DESCRIPTION
%doc %{rlibdir}/STAR/doc
%{rlibdir}/STAR/NAMESPACE
%{rlibdir}/STAR/Meta
%{rlibdir}/STAR/R
%{rlibdir}/STAR/help
%{rlibdir}/STAR/libs
%{rlibdir}/STAR/INDEX
%{rlibdir}/STAR/data
%{rlibdir}/STAR/demo

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.4-1
- initial package for Fedora