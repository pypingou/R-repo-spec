%global packname  LDcorSV
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          LDcorSV

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
The package provides a set of functions which aim is to propose four
measures of linkage disequilibrium: the usual r^2 measure, the r^2_S
measure (r^2 corrected by the structure sample), the r^2_V (r^2 corrected
by the relatedness of genotyped individuals), the r^2_VS measure (r^2
corrected by both the relatedness of genotyped individuals and the
structure of the sample).

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
%doc %{rlibdir}/LDcorSV/DESCRIPTION
%doc %{rlibdir}/LDcorSV/html
%{rlibdir}/LDcorSV/R
%{rlibdir}/LDcorSV/help
%{rlibdir}/LDcorSV/INDEX
%{rlibdir}/LDcorSV/NAMESPACE
%{rlibdir}/LDcorSV/data
%{rlibdir}/LDcorSV/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora