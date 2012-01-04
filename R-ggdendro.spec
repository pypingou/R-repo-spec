%global packname  ggdendro
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.01
Release:          1%{?dist}
Summary:          Tools for extracting dendrogram and tree diagram plot data for use with ggplot.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-01.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
This is a set of tools for dendrograms and tree plots using ggplot.  The
ggplot philosophy is to clearly separate data from the presentation. 
Unfortunately the plot method for dendrograms plots directly to a plot
device without exposing the data.  The ggdendro package resolves this by
making available functions that extract the dendrogram plot data.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.01-1
- initial package for Fedora