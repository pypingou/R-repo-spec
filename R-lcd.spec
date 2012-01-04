%global packname  lcd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Learn Chain graphs via Decomposition

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-igraph R-methods 
Requires:         R-MASS R-ggm 

BuildRequires:    R-devel tex(latex) R-igraph R-methods
BuildRequires:    R-MASS R-ggm 


%description
Functions for learning chain graphs (and as a special case, Bayesian
networks) via the decomposition approach.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.2-1
- initial package for Fedora