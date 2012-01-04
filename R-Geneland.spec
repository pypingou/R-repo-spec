%global packname  Geneland
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.3.0
Release:          1%{?dist}
Summary:          Detection of structure from multilocus genetic data.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RandomFields R-fields R-snow R-tcltk 

BuildRequires:    R-devel tex(latex) R-RandomFields R-fields R-snow R-tcltk 

%description
Stochastic simulation and MCMC inference of structure from genetic data.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.3.0-1
- initial package for Fedora