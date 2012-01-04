%global packname  rgenoud
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.7.3
Release:          1%{?dist}
Summary:          R version of GENetic Optimization Using Derivatives

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_5.7-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
A genetic algorithm plus derivative optimizer

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
%doc %{rlibdir}/rgenoud/CITATION
%doc %{rlibdir}/rgenoud/DESCRIPTION
%doc %{rlibdir}/rgenoud/doc
%doc %{rlibdir}/rgenoud/html
%{rlibdir}/rgenoud/libs
%{rlibdir}/rgenoud/help
%{rlibdir}/rgenoud/Meta
%{rlibdir}/rgenoud/INDEX
%{rlibdir}/rgenoud/R
%{rlibdir}/rgenoud/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.7.3-1
- initial package for Fedora