%global packname  hbim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Hill/Bliss Independence Model for Combination Vaccines

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-stats R-mvtnorm 

%description
Calculate expected relative risk and proportion protected assuming
normally distributed log10 transformed antibody dose for several component
vaccine. Uses Hill models for each component which are combined under
Bliss independence.

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
%doc %{rlibdir}/hbim/html
%doc %{rlibdir}/hbim/CITATION
%doc %{rlibdir}/hbim/DESCRIPTION
%doc %{rlibdir}/hbim/doc
%{rlibdir}/hbim/demo
%{rlibdir}/hbim/help
%{rlibdir}/hbim/Meta
%{rlibdir}/hbim/data
%{rlibdir}/hbim/R
%{rlibdir}/hbim/NAMESPACE
%{rlibdir}/hbim/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora