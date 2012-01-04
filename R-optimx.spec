%global packname  optimx
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.8.1
Release:          1%{?dist}
Summary:          A Replacement and Extension of the optim() Function

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011-8.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-numDeriv R-BB R-ucminf R-Rcgmin R-Rvmmin R-minqa R-setRNG 


BuildRequires:    R-devel tex(latex) R-numDeriv R-BB R-ucminf R-Rcgmin R-Rvmmin R-minqa R-setRNG



%description
Provides a replacement and extension of the optim() function to unify and
streamline optimization capabilities in R for smooth, possibly box
constrained functions of several or many parameters

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.8.1-1
- initial package for Fedora