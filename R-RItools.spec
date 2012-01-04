%global packname  RItools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Randomization inference tools

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-graphics R-stats R-lattice R-grid R-SparseM R-xtable 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-graphics R-stats R-lattice R-grid R-SparseM R-xtable 


%description
Tools for randomization inference.

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
%doc %{rlibdir}/RItools/CITATION
%doc %{rlibdir}/RItools/DESCRIPTION
%doc %{rlibdir}/RItools/doc
%doc %{rlibdir}/RItools/html
%doc %{rlibdir}/RItools/NEWS
%{rlibdir}/RItools/help
%{rlibdir}/RItools/R
%{rlibdir}/RItools/data
%{rlibdir}/RItools/NAMESPACE
%{rlibdir}/RItools/Meta
%{rlibdir}/RItools/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.11-1
- initial package for Fedora