%global packname  cmprsk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.2
Release:          1%{?dist}
Summary:          Subdistribution Analysis of Competing Risks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Estimation, testing and regression modeling of subdistribution functions
in competing risks, as described in Gray (1988), A class of K-sample tests
for comparing the cumulative incidence of a competing risk, Ann. Stat.
16:1141-1154, and Fine JP and Gray RJ (1999), A proportional hazards model
for the subdistribution of a competing risk, JASA, 94:496-509.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.2-1
- initial package for Fedora