%global packname  stam
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Spatio-Temporal Analysis and Modelling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-np R-sp 

BuildRequires:    R-devel tex(latex) R-np R-sp 

%description
stam is an evolving package that target on the various methods to conduct
Spatio-Temporal Analysis and Modelling,including Exploratory
Spatio-Temporal Analysis and Inferred Spatio-Temporal Modelling.

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
%doc %{rlibdir}/stam/DESCRIPTION
%doc %{rlibdir}/stam/COPYING
%doc %{rlibdir}/stam/html
%{rlibdir}/stam/Meta
%{rlibdir}/stam/INDEX
%{rlibdir}/stam/R
%{rlibdir}/stam/NAMESPACE
%{rlibdir}/stam/help

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora