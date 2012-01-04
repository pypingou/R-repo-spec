%global packname  movMF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.0
Release:          1%{?dist}
Summary:          Mixtures of von Mises Fisher Distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-skmeans R-clue 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-skmeans R-clue 


%description
Fit and simulate mixtures of von Mises Fisher distributions.

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
%doc %{rlibdir}/movMF/html
%doc %{rlibdir}/movMF/DESCRIPTION
%doc %{rlibdir}/movMF/doc
%{rlibdir}/movMF/R
%{rlibdir}/movMF/libs
%{rlibdir}/movMF/NAMESPACE
%{rlibdir}/movMF/Meta
%{rlibdir}/movMF/help
%{rlibdir}/movMF/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.0-1
- initial package for Fedora