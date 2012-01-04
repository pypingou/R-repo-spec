%global packname  pheatmap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Pretty Heatmaps

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package for drawing pretty heatmaps in R. The ordinary heatmap
function in R has several drawbacks, when it comes to producing
publication quality heatmaps. It is hard to produce pictures with
consistent text, cell and overall sizes and shapes. The function pheatmap
tries to alleviate the problems by offering more fine grained control over
heatmap dimensions and appearance.

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
%doc %{rlibdir}/pheatmap/DESCRIPTION
%doc %{rlibdir}/pheatmap/html
%{rlibdir}/pheatmap/INDEX
%{rlibdir}/pheatmap/NAMESPACE
%{rlibdir}/pheatmap/help
%{rlibdir}/pheatmap/Meta
%{rlibdir}/pheatmap/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora