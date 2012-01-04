%global packname  arulesViz
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          arulesViz - Visualizing Association Rules and Frequent Itemsets

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-arules R-MASS R-scatterplot3d R-vcd R-seriation R-igraph 


BuildRequires:    R-devel tex(latex) R-arules R-MASS R-scatterplot3d R-vcd R-seriation R-igraph



%description
Various visualization techniques for association rules and itemsets. The
packages also includes several interactive visualizations for rule
exploration. This package extends package arules.

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
%doc %{rlibdir}/arulesViz/doc
%doc %{rlibdir}/arulesViz/DESCRIPTION
%doc %{rlibdir}/arulesViz/html
%{rlibdir}/arulesViz/NAMESPACE
%{rlibdir}/arulesViz/INDEX
%{rlibdir}/arulesViz/help
%{rlibdir}/arulesViz/LICENSE
%{rlibdir}/arulesViz/Meta
%{rlibdir}/arulesViz/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora