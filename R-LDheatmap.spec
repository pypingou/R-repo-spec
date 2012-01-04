%global packname  LDheatmap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.9
Release:          1%{?dist}
Summary:          Graphical display of pairwise linkage disequilibria between SNPs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grid 
Requires:         R-genetics 

BuildRequires:    R-devel tex(latex) R-grid
BuildRequires:    R-genetics 


%description
Produces a graphical display, as a heat map, of measures of pairwise
linkage disequilibria between SNPs. Users may optionally include the
physical locations or genetic map distances of each SNP on the plot.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.9-1
- initial package for Fedora