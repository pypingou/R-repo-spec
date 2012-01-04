%global packname  LSD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.5
Release:          1%{?dist}
Summary:          Lots of Superior Depictions

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-gtools R-RColorBrewer R-colorRamps R-schoolmath R-ellipse 

BuildRequires:    R-devel tex(latex) R-MASS R-gtools R-RColorBrewer R-colorRamps R-schoolmath R-ellipse 

%description
Create lots of colorful plots in a plethora of variations ( try the
LSD.demo.tour() )

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
%doc %{rlibdir}/LSD/html
%doc %{rlibdir}/LSD/DESCRIPTION
%{rlibdir}/LSD/Meta
%{rlibdir}/LSD/NAMESPACE
%{rlibdir}/LSD/INDEX
%{rlibdir}/LSD/R
%{rlibdir}/LSD/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.5-1
- initial package for Fedora