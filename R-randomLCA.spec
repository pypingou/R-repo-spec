%global packname  randomLCA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.3
Release:          1%{?dist}
Summary:          Random Effects Latent Class Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-nlme R-boot 

BuildRequires:    R-devel tex(latex) R-lattice R-nlme R-boot 

%description
Fits random effects latent class models, as well as standard latent class

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
%doc %{rlibdir}/randomLCA/NEWS
%doc %{rlibdir}/randomLCA/html
%doc %{rlibdir}/randomLCA/DESCRIPTION
%doc %{rlibdir}/randomLCA/doc
%{rlibdir}/randomLCA/NAMESPACE
%{rlibdir}/randomLCA/data
%{rlibdir}/randomLCA/libs
%{rlibdir}/randomLCA/Meta
%{rlibdir}/randomLCA/R
%{rlibdir}/randomLCA/INDEX
%{rlibdir}/randomLCA/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.3-1
- initial package for Fedora