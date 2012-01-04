%global packname  HiveR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          2D and 3D Hive Plots for R

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-grid R-RColorBrewer R-rgl R-xtable R-bipartite R-RFOC R-sna 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-grid R-RColorBrewer R-rgl R-xtable R-bipartite R-RFOC R-sna 


%description
HiveR is an R package for creating and plotting 2D and 3D hive plots. Hive
plots are a unique method of displaying networks of many types in which
node properties are mapped to axes using meaningful properties rather than
being arbitrarily positioned.  The hive plot concept was invented by
Martin Krzywinski at the Genome Science Center (www.hiveplot.net/). 
Keywords: networks, food webs, linnet, systems biology, bioinformatics.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora