%global packname  evtree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Evolutionary Learning of Globally Optimal Trees

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-partykit 

BuildRequires:    R-devel tex(latex) R-partykit 

%description
Commonly used classification and regression tree methods like the CART
algorithm are recursive partitioning methods that build the model in a
forward stepwise search.  Although this approach is known to be an
efficient heuristic, the results of recursive tree methods are only
locally optimal, as splits are chosen to maximize homogeneity at the next
step only. An alternative way to search over the parameter space of trees
is to use global optimization methods like evolutionary algorithms. The
evtree package implements an evolutionary algorithm for learning globally
optimal classification and regression trees in R. CPU and memory-intensive
tasks are fully computed in C++ while the partykit package is leveraged to
represent the resulting trees in R, providing unified infrastructure for
summaries, visualizations, and predictions.

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
%doc %{rlibdir}/evtree/NEWS
%doc %{rlibdir}/evtree/html
%doc %{rlibdir}/evtree/doc
%doc %{rlibdir}/evtree/DESCRIPTION
%{rlibdir}/evtree/libs
%{rlibdir}/evtree/data
%{rlibdir}/evtree/R
%{rlibdir}/evtree/INDEX
%{rlibdir}/evtree/help
%{rlibdir}/evtree/NAMESPACE
%{rlibdir}/evtree/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora