%global packname  Heatplus
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{dist}
Summary:          Heatmaps with row and/or column covariates and colored clusters

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Display a rectangular heatmap (intensity plot) of a data matrix. By
default, both samples (columns) and features (row) of the matrix are
sorted according to a hierarchical clustering, and the corresponding
dendrogram is plotted. Optionally, panels with additional information
about samples and features can be added to the plot.

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
%doc %{rlibdir}/Heatplus/doc
%doc %{rlibdir}/Heatplus/DESCRIPTION
%doc %{rlibdir}/Heatplus/html
%doc %{rlibdir}/Heatplus/NEWS
%{rlibdir}/Heatplus/help
%{rlibdir}/Heatplus/Meta
%{rlibdir}/Heatplus/R
%{rlibdir}/Heatplus/INDEX
%{rlibdir}/Heatplus/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- Update to version 2.1.0

* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora