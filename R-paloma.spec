%global packname  paloma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Poisson Approximation for LOcal Motif Assessment

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mixer 


BuildRequires:    R-devel tex(latex) R-mixer



%description
Search over-represented motifs in a network under a statistical model

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
%doc %{rlibdir}/paloma/html
%doc %{rlibdir}/paloma/DESCRIPTION
%doc %{rlibdir}/paloma/NEWS
%{rlibdir}/paloma/help
%{rlibdir}/paloma/libs
%{rlibdir}/paloma/networks
%{rlibdir}/paloma/INDEX
%{rlibdir}/paloma/data
%{rlibdir}/paloma/demo
%{rlibdir}/paloma/NAMESPACE
%{rlibdir}/paloma/Meta
%{rlibdir}/paloma/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora