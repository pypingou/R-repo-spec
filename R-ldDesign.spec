%global packname  ldDesign
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Design of experiments for detection of linkage disequilibrium

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R package for design of experiments for association studies for detection
of linkage disequilibrium. Uses an existing deterministic power
calculation for detection of linkage disequilibrium between a bi-allelic
QTL and a bi-allelic marker, together with the Spiegelhalter and Smith
Bayes factor to generate designs with power to detect effects with a given
Bayes factor.

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
%doc %{rlibdir}/ldDesign/doc
%doc %{rlibdir}/ldDesign/DESCRIPTION
%doc %{rlibdir}/ldDesign/html
%{rlibdir}/ldDesign/data
%{rlibdir}/ldDesign/Meta
%{rlibdir}/ldDesign/R
%{rlibdir}/ldDesign/NAMESPACE
%{rlibdir}/ldDesign/help
%{rlibdir}/ldDesign/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora