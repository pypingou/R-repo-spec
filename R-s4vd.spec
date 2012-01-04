%global packname  s4vd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Biclustering via sparse singular value decomposition incorporating stability selection

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-biclust R-methods 

BuildRequires:    R-devel tex(latex) R-biclust R-methods 

%description
The main function s4vd performs a biclustering via sparse singular value
decomposition with a nested stability selection. The results is an biclust
object and thus all methods of the biclust package can be applied.

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
%doc %{rlibdir}/s4vd/DESCRIPTION
%doc %{rlibdir}/s4vd/html
%{rlibdir}/s4vd/help
%{rlibdir}/s4vd/INDEX
%{rlibdir}/s4vd/Meta
%{rlibdir}/s4vd/NAMESPACE
%{rlibdir}/s4vd/R
%{rlibdir}/s4vd/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora