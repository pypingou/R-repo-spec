%global packname  dae
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.7
Release:          1%{?dist}
Summary:          Functions useful in the design and ANOVA of experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-methods 

BuildRequires:    R-devel tex(latex) R-lattice R-methods 

%description
This package includes a number of functions that aid in generating
experimental designs and in examining their canonical efficiency factors.
It also includes functions that facilitate diagnostic checking after an
aov, especially when the Error function has been used in the call to aov.

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
%doc %{rlibdir}/dae/DESCRIPTION
%doc %{rlibdir}/dae/html
%{rlibdir}/dae/help
%{rlibdir}/dae/INDEX
%{rlibdir}/dae/Meta
%{rlibdir}/dae/data
%{rlibdir}/dae/R
%{rlibdir}/dae/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.7-1
- initial package for Fedora