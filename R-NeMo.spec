%global packname  NeMo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Exceptionnal Network Motifs in biological networks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
NeMo package aims to extract motifs which are occur more frequently than
expected in random, in a given network. The method used doesn't require
any Monte-Carlo based simulations. The number of motif occurences is
compared (p-value calculation) with well-suited count distribution
(compound Poisson distribution)

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
%doc %{rlibdir}/NeMo/NEWS
%doc %{rlibdir}/NeMo/html
%doc %{rlibdir}/NeMo/DESCRIPTION
%{rlibdir}/NeMo/R
%{rlibdir}/NeMo/help
%{rlibdir}/NeMo/INDEX
%{rlibdir}/NeMo/NAMESPACE
%{rlibdir}/NeMo/networks
%{rlibdir}/NeMo/libs
%{rlibdir}/NeMo/data
%{rlibdir}/NeMo/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora